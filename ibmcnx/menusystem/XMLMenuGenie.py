"""
Copyright (C) 2006  Daniel Mikusa

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""
import sys, xml.dom.minidom
import menusystem
"""Menu System

   Author:  Daniel Mikusa <dan@trz.cc>
Copyright:  April 4, 2006

A concrete implementation of the MenuGenie class.  This implementation is
stores the menu into an XML format.  More information on the exact format is
described below.
"""
class XMLMenuGenie(menusystem.MenuGenie):
	"""Loads and Saves Menu Systems to XML
	
	Implements the MenuGenie Interface allowing Menu Systems to be saved as
	XML files.  The format of the XML file is as follows:
		
		<menu>  -  represents a menu object (valid anywhere).  Must contain at
					least one choice object.  Title and prompt attributes are
					required.
			attribute list
				title  -  menu title
				prompt -  menu prompt
				data   -  Is this a data menu?

		<choice> - represents a choice object (only valid in menu tag).  A
					choice object may contain one and only one menu object.
					If the choice object contains a menu object, then the choice
					object becomes a sub-menu.  All attributes are valid for 
					regular choices and sub-menus.  Selector, description, and
					handler attributes are required.  If value is not specified
					then value will be set to equal selector.
			attribute list
				   selector -  used to determine if an object is selected
				description -  text to describe object to end user
				      value -  value representation passed to handler function
					handler -  name of python function to call when selected
	
	The use of other tags will trigger an error.  The use of unspecified
	attributes will not result in an error, they will be ignored.
	"""
	def __init__(self, loc, module_name):
		"""Initalize the XMLGenie Object
		
		Parameter loc sets the location of the XML file that will be read or
		written to.  Parameter module_name should be the module that defines 
		all of the functions that are used to handle menu choices.
		"""
		self.loc = loc
		self.module = __import__(module_name)
		
	def load(self):
		"""Load a Menu System from XML File
		
		Loads a Menu System from an XML file in the above specified format.  The
		parameter location is used to specify where to find the XML.  It can be
		a file object, the path to a local file, a URL, or the actual XML as
		a Python String.
		
		After the XML is processed, a Menu object is returned which contains
		the top level menu of the Menu System.
		"""
		fp = self._open('r')
		doc = xml.dom.minidom.parse(fp)
		fp.close()
		m = self._load(doc.documentElement)
		doc.unlink()
		return m
		
	def _load(self, head):
		"""Creates all menu object recursivly
		
		Starting at the document root, processes all menu tags thus building
		the menu system.
		
		Each meun tag is processed for it's attributes and contained choices.
		If one of the menu's choices is itself a [sub]menu, then recursivly
		process all of that menu's attributes and choices.
		
		The parameter to this function is the xml an menu tag object.  Start 
		with the document root, and recursivly progress down through submenus.
		
		The return value of this function is the head Menu object representing
		the entire menu system.
		"""
		choice_list = []
		for child in [x for x in head.childNodes if isinstance(x, xml.dom.minidom.Element) and x.tagName.lower() == 'choice']:
			c = menusystem.Choice()
			c.selector = child.getAttribute('selector')
			c.description = child.getAttribute('description')
			c.value = child.getAttribute('value')
			handler_name = child.getAttribute('handler')
			if handler_name != 'None':
				c.handler = getattr(self.module, handler_name)
			else:
				c.handler = None
			if child.hasChildNodes():
				tmp_m = [x for x in child.childNodes if isinstance(x, xml.dom.minidom.Element) and x.tagName.lower() == 'menu']
				try:
					c.subMenu = self._load(tmp_m[0])
				except IndexError:
					pass
			choice_list.append(c)
		if head.getAttribute('data').lower() == 'true':
			return menusystem.DataMenu(title=head.getAttribute('title'), prompt=head.getAttribute('prompt'))
		else:
			return menusystem.Menu(title=head.getAttribute('title'), prompt=head.getAttribute('prompt'), choice_list=choice_list)
	
	def save(self, menu):
		"""Saves a Menu System to XML File
		
		Saves a complete Menu System and all sub-menus to an XML file in the
		above specified format.  The parameter location is used to specify
		where the file is written to.  It can be a file object, the path to a
		local file or a string which will be set with the actual XML.
		
		Note unlike the load function, you cannot save to a URL.
		"""
		self.doc = xml.dom.minidom.Document()
		self.doc.appendChild(self._save(menu))
		fp = self._open('w')
		if fp:
			self.doc.writexml(fp,addindent='\t', newl='\n')
			fp.close()
		else:
			print 'Unable to output xml'
		self.doc.unlink()
		
	def _save(self, menu):
		"""Helper function for Saving
		
		Helper function to implement recursion for traversing the Menu System.
		
		Parameter menu is the current menu object.
		
		Returns the menu xml element
		"""
		m = self.doc.createElement('menu')
		m.setAttribute('title', str(menu.title))
		m.setAttribute('prompt', str(menu.prompt))
		m.setAttribute('data', 'False')
		try:
			for choice in menu.choices:
				c = self.doc.createElement('choice')
				c.setAttribute('selector', str(choice.selector))
				c.setAttribute('description', str(choice.description))
				c.setAttribute('value', str(choice.value))
				if choice.handler:
					c.setAttribute('handler', choice.handler.func_name)
				else:
					c.setAttribute('handler', 'None')
				if choice.subMenu:
					c.appendChild(self._save(choice.subMenu))
				m.appendChild(c)
		except AttributeError:
			m.setAttribute('data', 'True')
		return m
		
	def _open(self, mode):
		"""Open any location for reading or writing
		
		Helper function to open a file, url, or string for reading or writing.
		Used in conjunction with the save and load functions.
		
		Valid options for mode are 'w' for write and 'r' for read.  There is no
		need for append.
		
		The src parameter can be any valid url, file location, string, or file
		object.
		
		This method was borrowed from
			http://www.diveintopython.org/xml_processing/index.html, and
		modified slightly.
		
		The return value will be a file object unless there is an error.  In
		that case the return value will equal None.
		"""
		mode = mode.lower()
		if mode not in ('w', 'r'):
			return None
		
		if self.loc == '-' and mode == 'w':
			return sys.stdout
		if self.loc == '-' and mode == 'r':
			return sys.stdin
		
		if hasattr(self.loc, 'read') and mode == 'r':
			return self.loc
		if hasattr(self.loc, 'write') and mode == 'w':
			return self.loc
		
		if mode == 'r':
			import urllib
			try:
				return urllib.urlopen(self.loc)
			except (IOError, OSError):
				pass
		
		try:
			return open(self.loc, mode)
		except (IOError, OSError):
			pass

		if type(self.loc) == str:
			import StringIO
			return StringIO.StringIO(self.loc)
			
		return None
