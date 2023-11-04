#include <stdio.h>
#include <stdbool.h>

// State definition
typedef enum {
    POWER_UP,
    MOVE_FORWARD,
    TURN_RIGHT,
    TURN_LEFT,
    STOP,
    TURN_BACK,
    UNKNOWN_STATE
} State;

// Sensor inputs
bool F = false; // Front obstacle
bool L = false; // Left obstacle
bool R = false; // Right obstacle
bool D = false; // Dust sensor

State currentState = POWER_UP;

void printStateChange(const char* action, State nextState) {
    printf("%s. Transitioning to state: %d\n", action, nextState);
}

void powerUp() {
    printStateChange("Cleaner powered up", MOVE_FORWARD);
    // Initialize any necessary hardware or variables
}

void moveForward() {
    if (F && L) {
        printStateChange("Front and left obstacles detected. Turning right", TURN_RIGHT);
    } else if (F && R) {
        printStateChange("Front and right obstacles detected. Turning left", TURN_LEFT);
    } else if (F && L && R) {
        printStateChange("Front, left, and right obstacles detected. Stopping", STOP);
    } else {
        printf("Moving forward.\n");
    }
}

void turnRight() {
    printStateChange("Turning right", MOVE_FORWARD);
}

void turnLeft() {
    printStateChange("Turning left", MOVE_FORWARD);
}

void stop() {
    printStateChange("Stopped", TURN_BACK);
}

void turnBack() {
    printStateChange("Turning back", MOVE_FORWARD);
}

int main() {
    // Your main program logic here
    while (currentState != UNKNOWN_STATE) {
        switch (currentState) {
            case POWER_UP:
                powerUp();
                currentState = MOVE_FORWARD;
                break;
            case MOVE_FORWARD:
                moveForward();
                // Set F, L, and R based on sensor input
                // currentState might change within moveForward() based on sensors
                break;
            case TURN_RIGHT:
                turnRight();
                currentState = MOVE_FORWARD;
                break;
            case TURN_LEFT:
                turnLeft();
                currentState = MOVE_FORWARD;
                break;
            case STOP:
                stop();
                currentState = TURN_BACK;
                break;
            case TURN_BACK:
                turnBack();
                currentState = MOVE_FORWARD;
                break;
            default:
                break;
        }
    }

    return 0;
}
