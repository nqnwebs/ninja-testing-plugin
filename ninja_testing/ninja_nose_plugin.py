import os
import sys
import traceback

from nose.plugins.base import Plugin


err = sys.stderr


def extract_conflictive_lines(tb, limit=None, dirname=None):
    """
    return a list of tuples
    (filename, line_numbers) elated to a traceback

    ``tb`` is the traceback object

    ``limit`` the number of entries extracted. If is None all entries are extracted

    if ``dirname`` is given the list is filter to files in that path
    (useful for an option 'only show files of my project')
    """
    condition = lambda p: (os.path.dirname(p).startswith(dirname)
                           if dirname else True)
    return [(fn, ln) for (fn, ln, _, __) in traceback.extract_tb(tb, limit)
            if condition(fn)]


class NinjaNosePlugin(Plugin):
    name = 'ninja'

    def options(self, parser, env=os.environ):
        super(NinjaNosePlugin, self).options(parser, env=env)

    def configure(self, options, conf):
        super(NinjaNosePlugin, self).configure(options, conf)
        self.enabled = True

    def addFailure(self, test, err):
        conflict = (test.id(), extract_conflictive_lines(err[2]))
        import ipdb;ipdb.set_trace()
        #return conflict to update results widget

    def addError(self, test, err):
        conflict = (test.id(), extract_conflictive_lines(err[2]))
        import ipdb;ipdb.set_trace()
        #return conflict to update results widget
