
##SmartCare v0.1 - Community Clinic Appointment Booking System

appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    """Book an appointment after validating inputs and checking for double-booking."""
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    for appt in appointments:
        if appt["practitioner"] == practitioner_name and appt["time"] == appointment_time:
            raise ValueError(f"{practitioner_name} is already booked at {appointment_time}")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)
    print(f"Appointment booked: {patient_name} with {practitioner_name} at {appointment_time}")


def display_appointments():
    """Display all recorded appointments."""
    if not appointments:
        print("No appointments recorded.")
        return
    print("\n--- All Appointments ---")
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")


if __name__ == "__main__":
    print("SmartCare: Community Clinic Appointment Booking System\n")
    book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
    book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
    display_appointments()

    # Test double-booking
    try:
        book_appointment('Charlie Brown', 'Dr. John Doe', '2024-07-20 10:00 AM')
    except ValueError as e:
        print(f"\nError: {e}")