
import app as app_module

SAMPLE_TEXT = app_module.SAMPLE_TEXT


def test_home_page():
    response = app_module.app.test_client().get("/")
    assert response.status_code == 200


def test_typing_test_page():
    response = app_module.app.test_client().get("/test")
    assert response.status_code == 200


def test_results_page():
    response = app_module.app.test_client().get("/results")
    assert response.status_code == 200


def test_sample_text_is_passed_to_template(monkeypatch):
    captured = {}

    def fake_render_template(template_name, **context):
        captured["template"] = template_name
        captured.update(context)
        return "Test page"

    monkeypatch.setattr(app_module, "render_template", fake_render_template)

    response = app_module.app.test_client().get("/test")

    assert response.status_code == 200
    assert captured["template"] == "test.html"
    assert captured["sample_text"] == SAMPLE_TEXT


def test_unknown_route_returns_404():
    response = app_module.app.test_client().get("/unknown")
    assert response.status_code == 404
