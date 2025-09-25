import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()

df = pd.read_csv(args.input)
# Example transformation
df['processed'] = df[df.columns[0]].apply(lambda x: x.upper())
df.to_csv(args.output, index=False)
