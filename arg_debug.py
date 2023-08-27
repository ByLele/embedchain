s = '--condition=foo --testing --output-file abc.def -x a1 a2'
import  getopt
args = s.split()
print(args)  # ['--condition=foo', '--testing', '--output-file', 'abc.def', '-x', 'a1', 'a2']

optlist, args = getopt.getopt(args, 'x', [
    'condition=', 'output-file=', 'testing'])
print(optlist)  # [('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x', '')]
print(args)  # ['a1', 'a2']

