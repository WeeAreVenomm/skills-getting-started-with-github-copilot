import pytest

from src.app import activities


@pytest.mark.usefixtures("reset_activities")
def test_unregister_participant_removes_email_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert signup_response.status_code == 200
    assert email in activities[activity_name]["participants"]

    # Act
    unregister_response = client.delete(f"/activities/{activity_name}/participants/{email}")

    # Assert
    assert unregister_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
