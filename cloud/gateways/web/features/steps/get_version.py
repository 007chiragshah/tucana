from behave import then, when


@when('I send a GET request to "/version"')
def step_impl(context):
    response = context.client.get("/web/version")
    context.response = response


@then("the response status code should be 200")
def step_impl(context):
    assert (
        context.response.status_code == 200
    ), f"Expected 200 but got {context.response.status_code}"


@then('the response should contain the "version" field')
def step_impl(context):
    response_json = context.response.json()
    assert "version" in response_json, "Response JSON does not contain 'version' field"


@then('the "version" field should be `local`')
def step_impl(context):
    response_json = context.response.json()
    assert (
        response_json["version"] == "local"
    ), f"Response JSON 'version' field is `{response_json['version']}`"
