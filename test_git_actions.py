class TestGitActions:
    name = "ahmed ali"
    age = 15

    def test_student_name(self):
        assert self.name == "ahmed ali"

    def test_student_age(self):
        assert self.age == 15
