from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


class PDFExporter:
    """
    Export cyber threat report to PDF.
    """

    def export(
        self,
        report: dict,
        filename: str = "Threat_Report.pdf",
    ):

        document = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph("<b>Cyber Threat Analysis Report</b>", styles["Title"])
        )

        content.append(
            Paragraph(f"<b>Risk Level:</b> {report['risk']}", styles["Heading2"])
        )

        content.append(
            Paragraph("<b>Summary</b>", styles["Heading2"])
        )

        content.append(
            Paragraph(report["summary"], styles["BodyText"])
        )

        content.append(
            Paragraph("<b>Detected MITRE Techniques</b>", styles["Heading2"])
        )

        for technique in report["techniques"]:

            text = f"""
            <b>{technique['id']}</b><br/>
            {technique['name']}<br/>
            Tactic: {technique['tactic']}<br/>
            Platform: {technique['platform']}<br/>
            Similarity: {technique['similarity']}%
            """

            content.append(
                Paragraph(text, styles["BodyText"])
            )

        content.append(
            Paragraph("<b>Recommendations</b>", styles["Heading2"])
        )

        for recommendation in report["recommendations"]:

            content.append(
                Paragraph(f"• {recommendation}", styles["BodyText"])
            )

        document.build(content)

        return filename