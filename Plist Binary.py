import sublime, sublime_plugin
import os

class ToggleBinaryCommand(sublime_plugin.TextCommand):
  def run_(self, args):

    fname = self.view.file_name()
    if os.path.splitext(fname)[1].lower() != ".plist":
      sublime.error_message("%s: Not a *.plist file!" % PACKAGE_NAME)
      return

    if self.view.is_dirty():
      sublime.error_message("%s: Can't encode an unsaved file!" % PACKAGE_NAME)
      return

    if self.view.substr(sublime.Region(0, 5)) == "<?xml":
      os.system("plutil -convert binary1 " + fname)
      self.view.set_syntax_file("Packages/Text/Plain text.tmLanguage")
    else:
      os.system("plutil -convert xml1 " + fname)
      self.view.set_syntax_file("Packages/XML/XML.tmLanguage")

    self.view.run_command('revert');