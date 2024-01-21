def AlphaFoldXploR_read(zfile):
    with ZipFile(zfile, 'r') as fz:
        for zip_info in fz.infolist():
            if zip_info.filename[-1] == '/':
                continue
            tab = os.path.basename(zip_info.filename)
            if tab.endswith(".json"):
                zip_info.filename = os.path.basename(zip_info.filename)
                lista1 = fz.extract(zip_info, "archivos_json")

    with ZipFile(zfile, 'r') as fz:
        for zip_info in fz.infolist():
            if zip_info.filename[-1] == '/':
                continue
            tab = os.path.basename(zip_info.filename)
            if tab.endswith(".pdb"):
                zip_info.filename = os.path.basename(zip_info.filename)
                lista2 = fz.extract(zip_info, "archivos_pdb")

