from todo import TodoManager as td
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
todo_manager = td()

