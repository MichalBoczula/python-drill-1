Feature: API health and documentation
  As an API consumer
  I want the service and its contract to be discoverable

  Scenario: The API reports liveness
    Given a running API
    When I GET "/health/live"
    Then the status is 200
    And the body indicates liveness

  Scenario: The API serves OpenAPI documentation
    Given a running API
    When I GET "/openapi.json"
    Then the status is 200
    And the OpenAPI document includes the health routes
