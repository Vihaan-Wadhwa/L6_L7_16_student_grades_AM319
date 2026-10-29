import pytest
from student_grades import letter_grade, final_marks, exam_eligibility

# Test cases for branch coverage: every if/elif/else decision is taken both ways.


# letter_grade
def test_negative_marks():
    with pytest.raises(ValueError):
        letter_grade(-1)

def test_marks_above_100():
    with pytest.raises(ValueError):
        letter_grade(101)

def test_s_grade():
    assert letter_grade(90) == "S"

def test_a_grade():
    assert letter_grade(80) == "A"

def test_b_grade():
    assert letter_grade(70) == "B"

def test_c_grade():
    assert letter_grade(60) == "C"

def test_d_grade():
    assert letter_grade(50) == "D"

def test_e_grade():
    assert letter_grade(40) == "E"

def test_f_grade():
    assert letter_grade(39) == "F"


# final_marks
def test_internal_out_of_range():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)

def test_external_out_of_range():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)

def test_final_marks_without_project():
    assert final_marks(30, 50, False) == 80

def test_final_marks_with_project_under_100():
    assert final_marks(30, 50, True) == 85

def test_final_marks_project_capped_at_100():
    assert final_marks(40, 60, True) == 100


# exam_eligibility
def test_blocked():
    assert exam_eligibility(90, False, False) == "blocked"

def test_eligible():
    assert exam_eligibility(75, True, False) == "eligible"

def test_eligible_with_medical():
    assert exam_eligibility(65, True, True) == "eligible"

def test_detained_without_medical():
    assert exam_eligibility(70, True, False) == "detained"

def test_detained_low_attendance():
    assert exam_eligibility(50, True, True) == "detained"
