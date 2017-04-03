import re

first_to_lower = lambda s: s[:1].lower() + s[1:] if s else ''

first_to_upper = lambda s: s[:1].upper() + s[1:] if s else ''

get_number = lambda s: filter(str.isdigit, s)

fold_s = lambda f, l: '' if not l else f(l[0]) + fold_s(f, l[1:])

def to_snake_case(name):
  string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()

def to_res(name):
  string = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1-\2', string).lower()

def replace_all_tokens(text, tokens):
  for token, replacement in tokens.iteritems():
    if replacement:
      text = text.replace('{{{' + token + '}}}', replacement)
    else:
      text = text.replace('{{{' + token + '}}}\n', '')
      text = text.replace('{{{' + token + '}}}', '')
  return text