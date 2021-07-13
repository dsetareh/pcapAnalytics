import pyshark, subprocess, json, os

for filename in os.listdir("./pcaps"):
    full_pcap_filename = "./pcaps/" + filename
    pcap = pyshark.FileCapture(full_pcap_filename)
    try:
        num_packets = subprocess.check_output(['tshark', '-r', full_pcap_filename]).count(b'\n')
    except subprocess.CalledProcessError as exc:
        num_packets = exc.output.count(b'\n') - 1


    packets = []
    for idx, p in enumerate(pcap):
        if idx == num_packets:
            break
        packets.append(p['mac-lte']._all_fields)

    with open('json/' + filename[0:-5] + '.json', 'w') as outfile:
        json.dump(packets, outfile)
