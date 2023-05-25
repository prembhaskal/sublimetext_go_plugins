import sublime
import sublime_plugin
import subprocess


class GoFumportsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        sublime.status_message("got full path")
        print("full name of file is " + filename)
        subprocess.run(["gofmt", "-w", filename], capture_output=True)
        subprocess.run(["goimports", "-w", filename], capture_output=True)

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)
