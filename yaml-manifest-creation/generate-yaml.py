from jinja2 import Environment, FileSystemLoader
import yaml
import os
if __name__ == "__main__":
  values = yaml.safe_load(open('./value.yaml'))
    # Load templates file from templtes folder
  env = Environment(loader = FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
  template = env.get_template('template.j2')
  dir = 'resultfile'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
for deployment in values["deployments"]:
  file=open("resultfile/dep-"+deployment['name']+".yaml", "w")
  file.write(template.render(deployment))
  file.close()