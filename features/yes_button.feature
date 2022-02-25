Feature: Yes Button
    Press the Yes button to stop the movie queue, and give a message
    to give congradulations

    Scenario: Yes working normally
        Given A movie is currently displayed
            When The Yes button is pressed
            Then A congratulations message is displayed