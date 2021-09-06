#Import inside a class

class FromStandardLibrary():
    import abc #import just one module in one line

    import aifc, antigravity, argparse, array, asynchat, asyncio #import some modules in one line

    from calendar import Calendar #from ... import just one class
    from calendar import week #from ... import just one function
    from calendar import WEDNESDAY #from ... import just one constant
    from calendar import day_name #from ... import just one variable
    from unittest import async_case  #from ... import just one module
    from os import __file__  #from ... import just one __something__

    from code import InteractiveConsole, InteractiveInterpreter #from ... import some classes
    from ast import parse, iter_child_nodes, dump #from ... import some functions
    from colorsys import ONE_SIXTH, ONE_THIRD, TWO_THIRD #from ... import some constants
    from cmath import e, pi #from ... import some variables
    from unittest import mock, main, case #from ... import some modules
    from os import __annotations__, __doc__  #from ... import some __something__ 
    from csv import Dialect, Error, reader, get_dialect, QUOTE_ALL, QUOTE_NONE #from ... import some attributes

    # Não é permitido dentro de um classe:
    # from base64 import * #from ... import *

    import asyncio.constants #import just one module from a package

    import asyncio.coroutines, asyncio.queues, asyncio.events, asyncio.protocols, asyncio.threads #import modules from some packages

    from xml.dom import HierarchyRequestErr  #from package import just one class
    from email.utils import getaddresses #from package import just one function
    from xml.dom import INDEX_SIZE_ERR #from package import just one constant
    from tkinter.filedialog import dialogstates  #from package import just one variable
    from xml.dom import domreg #from package import just one module
    from xml.dom import __builtins__ #from package import just one __something__

    from email.errors import BoundaryError, CharsetError #from package import some classes
    from test.support.script_helper import assert_python_failure, assert_python_ok, make_script #from package import some functions
    from idlelib.help_about import  BOTTOM, TOP #from package import some constants
    from turtledemo.minimal_hanoi import addshape, bk, clearscreen #from package import some variables
    from lib2to3.fixes.fix_unicode import fixer_base, token #from package import some modules
    from lib2to3.fixes.fix_unicode import __builtins__, __cached__ #from package import some  __something__
    from multiprocessing.dummy import DummyProcess, Array, connection  #from package import some  attributes

    # Não é permitido dentro de um classe:
    # from http.cookies import *

class FromExternalLibrary():
    import pytest #import just one module in one line

    import requests, redis, pandas #import some modules in one line

    from flask import Flask  #from ... import just one class
    from flask import  redirect  #from ... import just one function
    from numpy import Infinity #from ... import just one constant
    from numpy import abs #from ... import just one variable
    from numpy  import  distutils #from ... import just one module
    from flask import  __loader__ #from ... import just one __something__

    from pymongo import  MongoClient, ReplaceOne, DeleteOne  #from ... import some classes
    from pymongo import  get_version_string, has_c #from ... import some functions
    from pymongo import ALL, ASCENDING, DESCENDING #from ... import some constants
    from sqlalchemy import  asc, desc  #from ... import some variables
    from PIL import Image, GifImagePlugin  #from ... import some modules
    from PIL import __package__, __version__, __spec__  #from ... import some __something__ 
    from pymongo import UpdateOne, server, HASHED, version #from ... import some attributes

    # Não é permitido dentro de um classe:
    #from pygame import * #from ... import *


    import AWSIoTPythonSDK.MQTTLib #import just one module from a package


    import scipy.special, moviepy.editor #import modules from some packages


    from bs4.element import BeautifulSoup  #from package import just one class
    from matplotlib.pyplot import box #from package import just one function
    from bs4.element import  DEFAULT_OUTPUT_ENCODING #from package import just one constant
    from bs4.element import whitespace_re  #from package import just one variable
    from matplotlib.pyplot import style #from package import just one module
    from matplotlib.pyplot import __name__ #from package import just one __something__


    from selenium.webdriver.common.proxy import Proxy, ProxyType  #from package import some classes
    from matplotlib.pyplot import plot, bar, axes  #from package import some functions
    from scipy.constants import c, golden, g, Planck #from package import some constants
    from django.db import connection, connections  #from package import some variables
    from selenium.webdriver import remote, android, chrome  #from package import some modules
    from django.forms import __annotations__, __cached__  #from package import some  __something__
    from django.forms import all_valid, BaseForm, models, __doc__ #from package import some  attributes

    # Não é permitido dentro de um classe:
    #from emoji.core import *

class FromMyOwnModules():
    import mymodule #import just one module in one line

    import datetimeExample, cloneRepository, mongoExample #import some modules in one line

    from usuario import Usuario #from ... import just one class
    from area import circle #from ... import just one function
    from area import PI #from ... import just one constant
    from mymodule2 import a #from ... import just one variable
    from mymodule2 import area  #from ... import just one module
    from usuario import __builtins__  #from ... import just one __something__

    from mediador import MediadorDoAdministrador, MediadorDoCafeicultor, MediadorInterface #from ... import some classes
    from area import triangle, square, rectangle #from ... import some functions
    from constants import PI, G, RAIZ3, RAIZ2 #from ... import some constants
    from mymodule2 import b, c #from ... import some variables
    from mediador import sacaCafe, bancoDeDados #from ... import some modules
    from mediador import  __annotations__, __cached__ #from ... import some __something__ 
    from mediador import  ABC, cafeicultor, annotations, __package__  #from ... import some attributes

    # Não é permitido dentro de um classe:
    #from awspubsub import * #from ... import *

    import RandomFiles.client #import just one module from a package

    import RandomFiles.regexExample, RandomFiles.plotExample, RandomFiles.mysqlExample #import modules from some packages

    from RandomFiles.entidades.administrador import Administrador  #from package import just one class
    from RandomFiles.webScrapping import cotacaoCafe #from package import just one function
    from RandomFiles.jsonExample import MYJSON  #from package import just one constant
    from RandomFiles.server import adress  #from package import just one variable
    from RandomFiles.entidades.cafeicultor import usuario #from package import just one module
    from RandomFiles.server import __doc__ #from package import just one __something__

    from RandomFiles.exception.exception import SomeException, RequestException #from package import some classes
    from RandomFiles.volume import cubo, esfera, paralelepipedo #from package import some functions
    from RandomFiles.defaultAcess import PASSWORD, USER #from package import some constants
    from RandomFiles.bancoDeDados import listaCafe, listaCafeicultor #from package import some variables
    from RandomFiles.entidades.administrador import bancoDeDados, usuario #from package import some modules
    from RandomFiles.bancoDeDados import __package__, __cached__ #from package import some  __something__
    from RandomFiles.random import Usuario, getNome, MYCONSTANT, myvariable  #from package import some  attributes

    # Não é permitido dentro de um classe:
    #from unittest.classes.testAdministrador import *