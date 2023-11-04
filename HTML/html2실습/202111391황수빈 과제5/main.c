#include <stdio.h>
#include <stdbool.h>

// 상태 정의
typedef enum {
    POWER_UP,
    MOVE_FORWARD,
    TURN_RIGHT,
    TURN_LEFT,
    STOP,
    TURN_BACK
} State;

// 센서 입력 정의
bool F; // Front obstacle
bool L; // Left obstacle
bool R; // Right obstacle
bool D; // Dust sensor

State currentState = POWER_UP;

void powerUp() {
    // Power up the cleaner
    printf("Cleaner powered up.\n");
    currentState = MOVE_FORWARD;
}

void moveForward() {
    printf("Moving forward.\n");
    // Check sensor inputs to decide next state
    if (F && L) {
        currentState = TURN_RIGHT;
    } else if (F && R) {
        currentState = TURN_LEFT;
    } else if (F && L && R) {
        currentState = STOP;
    }
}

void turnRight() {
    printf("Turning right.\n");
    currentState = MOVE_FORWARD;
}

void turnLeft() {
    printf("Turning left.\n");
    currentState = MOVE_FORWARD;
}

void stop() {
    printf("Stopped.\n");
    currentState = TURN_BACK;
}

void turnBack() {
    printf("Turning back.\n");
    currentState = MOVE_FORWARD;
}

int main() {
    while (1) {
        switch (currentState) {
            case POWER_UP:
                powerUp();
                break;
            case MOVE_FORWARD:
                moveForward();
                break;
            case TURN_RIGHT:
                turnRight();
                break;
            case TURN_LEFT:
                turnLeft();
                break;
            case STOP:
                stop();
                break;
            case TURN_BACK:
                turnBack();
                break;
            default:
                printf("Unknown state.\n");
                return 0;
        }
    }
    return 0;
}
