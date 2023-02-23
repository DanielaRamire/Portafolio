import pytest
import os
import io
from ver2_portafolio.portafolio.models import Project

image_path = os.path.join(os.path.dirname(__file__), 'ver2_portafolio/portafolio/images/python.png')
with open(image_path, 'rb') as f:
    image_data = io.BytesIO(f.read()) 

def test_project_creation():
    project = Project.objects.create(
        title='unprojecto',
        description='este es un proyecto',
        image=image_data,
        tools='angular',
        url='https://www.google.com/'
    )
    assert project.title == 'unprojecto'
