import os

badHash='c1a4be04b972b6c17db242fc37752ad517c29402'
goodHash='e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'

os.system('git bisect start %s %s' % (badHash, goodHash))
os.system('git bisect run python manage.py test')
os.system('git bisect reset')
