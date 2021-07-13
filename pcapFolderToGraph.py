import subprocess, json, os, time
import plotly.graph_objects as go

time_deltas = []
increment = 0

for filename in os.listdir(
        "/home/dsetareh/pyshark/sampleGraphs/fuzzLogs/pcap/1958"):
    increment += 1
    full_pcap_filename = "/home/dsetareh/pyshark/sampleGraphs/fuzzLogs/pcap/1958/" + filename

    try:
        packet_timings = subprocess.check_output([
            'tshark', '-r', full_pcap_filename, '-e', 'udp.time_delta',
            '-Tfields'
        ],
                                                 start_new_session=False)
    except subprocess.CalledProcessError as exc:
        packet_timings = exc.output.split(b'\n')
        ptFloat = []
        for timing in packet_timings:
            if (len(timing) < 2):
                continue
            ptFloat.append(float(timing))

    time_deltas.append(ptFloat[2])

print(time_deltas)
fig = go.Figure(data=go.Bar(y=time_deltas))
fig.write_html('time_deltas_1958.html', auto_open=True)
with open('raw_time_deltas_1958.json', 'w') as outfile:
    json.dump(time_deltas, outfile)