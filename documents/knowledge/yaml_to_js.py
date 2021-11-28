import os
import yaml


codepage = "λƛ¬∧⟑∨⟇÷×«␤»°•ß†€"
codepage += "½∆ø↔¢⌐æʀʁɾɽÞƈ∞¨␠"
codepage += "!\"#$%&'()*+,-./01"
codepage += "23456789:;<=>?@A"
codepage += "BCDEFGHIJKLMNOPQ"
codepage += "RSTUVWXYZ[\\]`^_abc"
codepage += "defghijklmnopqrs"
codepage += "tuvwxyz{|}~↑↓∴∵›"
codepage += "‹∷¤ð→←βτȧḃċḋėḟġḣ"
codepage += "ḭŀṁṅȯṗṙṡṫẇẋẏż√⟨⟩"
codepage += "‛₀₁₂₃₄₅₆₇₈¶⁋§ε¡"
codepage += "∑¦≈µȦḂĊḊĖḞĠḢİĿṀṄ"
codepage += "ȮṖṘṠṪẆẊẎŻ₌₍⁰¹²∇⌈"
codepage += "⌊¯±₴…□↳↲⋏⋎꘍ꜝ℅≤≥"
codepage += "≠⁼ƒɖ∪∩⊍£¥⇧⇩ǍǎǏǐǑ"
codepage += "ǒǓǔ⁽‡≬⁺↵⅛¼¾Π„‟"

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
ELEMENTS_YAML = os.path.join(CURR_DIR, "elements.yaml")
JS_FILE = os.path.join(CURR_DIR, "../../static/parsed_yaml.js")

with open(ELEMENTS_YAML, "r", encoding="utf-8") as elements:
    data = yaml.safe_load(elements)

with open(JS_FILE, mode="w", encoding="utf-8") as out:
    out.write("// Very important: DON'T EDIT THIS FILE!\n")
    out.write("// It's autogenerated\n")
    out.write("// See yaml_to_js.py\n\n")
    out.write(f"var codepage = {codepage!r}\n")
    out.write("var codepage_descriptions = []\n\n")
    for element in data:

        if "element" in element and len(element["element"]) == 2:
            out.write(
                "codepage_descriptions["
                + str(codepage.index(element["element"][1]))
                + "] += `\n"
            )
            out.write(
                str(element["element"]) + " (" + str(element["name"]) + ")\n"
            )
            out.write(str(element["description"]) + "\n")
            if "overloads" in element:
                for overload in element["overloads"]:
                    data_types = map(
                        lambda x: " ".join(x),
                        zip(overload.split("-"), "abc"),
                    )
                    out.write(
                        ", ".join(data_types)
                        + " -> "
                        + str(element["overloads"][overload]).replace(
                            "`", "\\`"
                        )
                        + "\n"
                    )
            out.write("`\n")
        else:
            out.write("codepage_descriptions.push(`")
            out.write(str(element["name"]) + "\n")
            out.write(str(element["description"]).replace("`", "\\`") + "\n")
            if "overloads" in element:
                for overload in element["overloads"]:
                    data_types = map(
                        lambda x: " ".join(x),
                        zip(overload.split("-"), "abc"),
                    )
                    out.write(
                        ", ".join(data_types)
                        + " -> "
                        + str(element["overloads"][overload]).replace(
                            "`", "\\`"
                        )
                        + "\n"
                    )
            out.write("`)\n\n")
