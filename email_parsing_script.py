#comcast pre-parse
def preprocess_container(container):
    new_artifacts = []
    for artifact in container.get('artifacts', []):
        cef = artifact.get('cef')
        fromEmail = cef.get('fromEmail')
        toEmail = cef.get('toEmail')
        if fromEmail:
            artifact['cef']['fromEmail'] = fromEmail.split('<')[1].split('>')[0].lower() #Syed added .lower()
        if toEmail:
            artifact['cef']['toEmail'] = toEmail.split('<')[1].split('>')[0].lower() #Syed added .lower()
        new_artifacts.append(artifact)
    if new_artifacts:
        new_artifacts[-1]['run_automation'] = True
    container['artifacts'] = new_artifacts
    return container
