from src.dependency import Dependency
from src.kata import Kata


class TestKata:
    def test_value_should_work_with_dependency_implementation(self):
        dependency = Dependency()
        kata = Kata(dependency)

        actual = kata.value()

        assert actual == 1
