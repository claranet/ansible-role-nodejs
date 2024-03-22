import os

  
def test_npm(host):
  npm_list = host.check_output("""npm list --json --global | jq -r '.dependencies | to_entries[] | select((.value.missing // false   | not) and (.value.invalid // false | not)) | .key + "@" + .value.version'""")
  assert 'chance@1.1.3' in npm_list
  assert 'coffeescript@' in npm_list
  assert 'enzyme@' not in npm_list
