from requests import Response
import json



class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}, Actual: {response.status_code}, URL: {response.url}"

    @staticmethod
    def assert_json_has_key(response, name):
        try:
            response_json = response.json()
        except ValueError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_json, \
            f"Response JSON doesn't have key '{name}'. JSON: {response_json}"
