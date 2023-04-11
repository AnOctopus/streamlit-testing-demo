from streamlit.testing.script_interactions import InteractiveScriptTests


class AppTest(InteractiveScriptTests):
    def test_widgets(self):
        script = self.script_from_filename(__file__, "streamlit_app.py")
        sr = script.run()
        assert sr.get("header")[0].value == "My Streamlit App"
        # sidebar is after the main elements
        assert sr.get("markdown")[1].value == "Welcome back!"
        assert sr.get("multiselect")[0].value == []
        assert sr.get("markdown")[0].value == "Chose 0 widgets"

        sr2 = sr.get("multiselect")[0].select("checkbox").select("radio").run()
        assert sr2.get("checkbox")[0].value == False
        assert sr2.get("radio")[0].value == "foo"
        assert sr2.get("markdown")[0].value == "Chose 2 widgets"

        sr2.get("checkbox")[0].check()
        sr2.get("radio")[0].set_value("baz")
        sr3 = sr2.run()
