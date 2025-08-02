"""Placeholder constraint solver for the speech therapy scheduler."""


def solve_schedule(therapists, patients):
    """Return an empty schedule structure for each therapist.

    Args:
        therapists (list[dict]): Therapist data.
        patients (list[dict]): Patient data.

    Returns:
        dict: Mapping therapist_id -> {"name": str, "schedule": dict}
    """
    schedule = {}
    for therapist in therapists:
        schedule[therapist["id"]] = {
            "name": therapist["name"],
            "schedule": {}
        }
    return schedule
