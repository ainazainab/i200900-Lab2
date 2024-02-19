import pytest
from main import StudentsInMLOps

@pytest.fixture
def students_instance():
    return StudentsInMLOps()

def test_enrollStudents(students_instance):
    students_instance.enrollStudents(5)
    assert students_instance.getTotalStrength() == 5

def test_dropStudents(students_instance):
    students_instance.enrollStudents(10)
    students_instance.dropStudents(3)
    assert students_instance.getTotalStrength() == 7

def test_getClassName(students_instance):
    assert students_instance.getClassName() == "StudentsInMLOps"
