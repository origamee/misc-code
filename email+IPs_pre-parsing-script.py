#comcast pre-parse
import re
def preprocess_container(container):

    IP_REGEX = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    IPV6_REGEX = r'\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|'
    IPV6_REGEX += r'(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))'
    IPV6_REGEX += r'|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|'
    IPV6_REGEX += r'(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|'
    IPV6_REGEX += r'(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|'
    IPV6_REGEX += r'(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|'
    IPV6_REGEX += r'(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|'
    IPV6_REGEX += r'(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*'

    ip_regexc = re.compile(IP_REGEX)
    ipv6_regexc = re.compile(IPV6_REGEX)

    new_artifacts = []
    for artifact in container.get('artifacts', []):
        cef = artifact.get('cef')
        fromEmail = cef.get('fromEmail')
        toEmail = cef.get('toEmail')
        if fromEmail:
            artifact['cef']['fromEmail'] = fromEmail.split('<')[1].split('>')[0]
        if toEmail:
            artifact['cef']['toEmail'] = toEmail.split('<')[1].split('>')[0]
        new_artifacts.append(artifact)
        emailHeaders = cef.get('emailHeaders')
        if emailHeaders:
            received = emailHeaders.get('Received')
            if received:
                ips_in_mail = re.findall(ip_regexc, received)
                ip6_in_mail = re.findall(ipv6_regexc, received)
                for ip in ips_in_mail:
                    new_artifacts.append({
                        'name': 'IP Artifact',
                        'cef': {
                            'sourceAddress': ip
                                }
                        })
                for ip in ip6_in_mail:
                    new_artifacts.append({
                        'name': 'IP Artifact',
                        'cef': {
                            'sourceAddress': ip
                                }
                        })
    if new_artifacts:
        new_artifacts[-1]['run_automation'] = True
    container['artifacts'] = new_artifacts
    return container
