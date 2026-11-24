import click

import frappe

import healthcare


def execute():
	def major_version(v: str) -> str:
		return v.split(".")[0]

	frappe_version = major_version(frappe.__version__)
	healthcare_version = major_version(healthcare.__version__)

	WIKI_URL = "https://docs.thinknxg.com/thinknxghealth"

	if frappe_version == "15" and healthcare_version == "16":
		message = f"""
			The `develop` branch of thinkNXG Health is no longer compatible with thinkNXG Framework & thinkNXG ERP's `version-15`.
			Since you are using thinkNXG ERP/thinkNXG Framework `version-15` please switch thinkNXG Health app's branch to `version-15` and then proceed with the update.\n\t
			You can switch the branch by following the steps mentioned here: {WIKI_URL}
		"""
		click.secho(message, fg="red")

		frappe.throw(message)  # nosemgrep
