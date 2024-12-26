from pathlib import Path
from tomllib import load as toml_load

class Pgen:
    def __init__(self, **kwargs):
        self.source_dir = Path(kwargs.get('source_dir'))
        self.output_dir = Path(kwargs.get('output_dir'))
    
    def __str__(self):
        return f"source: {self.source_dir} \npublish: {self.output_dir}"

    def version(self) -> str:
        with open('pyproject.toml', 'rb') as f:
            data = toml_load(f)

        return data.get('project').get('version')

if __name__=="__main__":

    p = Pgen(source_dir="sample", output_dir="wwwsite")

    print(p)
    print(p.version())
    
