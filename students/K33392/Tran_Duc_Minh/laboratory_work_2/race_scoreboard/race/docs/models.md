
# Models in `models.py`

Below are the Django models defined in the `models.py` file of your project:

## Team

- `name` (CharField): Maximum length of 100 characters.
- `description` (TextField): A text field for describing the team.
- `__str__` method returns the team name.

## Race

- `race_name` (CharField): Maximum length of 100 characters.
- `race_date` (DateField): Date of the race.
- `registration_deadline` (DateField): Deadline for registration.
- `__str__` method returns the race name.

## Participant

- `user` (ForeignKey to User): Reference to the user associated with the participant.
- `team` (ForeignKey to Team): Reference to the team the participant belongs to.
- `car_description` (TextField): A text field for describing the participant's car.
- `experience` (IntegerField): Integer field for participant's experience.
- `registered_races` (ManyToManyField to Race through 'RaceRegistration'): References to the races a participant is registered in.
- `__str__` method returns a string containing the participant's username and team name.

## RaceRegistration

- `race` (ForeignKey to Race): Reference to the race being registered.
- `participant` (ForeignKey to Participant): Reference to the participant registering for the race.
- `registration_date` (DateField with auto_now_add=True): Date when the registration is added.

## RaceResult

- `race` (ForeignKey to Race): Reference to the race the result belongs to.
- `participant` (ForeignKey to Participant): Reference to the participant achieving the result.
- `race_time` (DurationField): The time taken to complete the race.
- `finishing_position` (PositiveIntegerField): The finishing position in the race.
- `__str__` method returns a string with the participant's username and race name.

## Commentator

- `user` (OneToOneField to User): Reference to the user associated with the commentator.

## Comment

- `race` (ForeignKey to Race): Reference to the race being commented on.
- `commentator` (ForeignKey to Commentator): Reference to the commentator.
- `comment_date` (DateTimeField with auto_now_add=True): Date and time when the comment is added.
- `comment_content` (TextField): The content of the comment.
- `comment_type` (CharField with choices): Choices for different comment types.
- `rating` (PositiveIntegerField with max value validation to 10): Rating for the comment.

These models represent the structure of your Django application and define the relationships between different entities within your project.
