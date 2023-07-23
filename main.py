import pandas as pd

def read_player(player, type):
    info = (
        f"Name: {player[0]}, "
        f"PPG: {player[2]}, "
        f"TRB: {player[3]}, "
        f"AST: {player[4]}"
    )
    return { 'info': info, 'type': type }

def transform_df(df, type):
    player_list = df.values.tolist()
    output = map(lambda x: read_player(x, type), player_list)
    outputlist = list(output)
    return pd.DataFrame(outputlist)

def main():
    star_df = pd.read_csv ('stars.csv')
    scrub_df = pd.read_csv ('scrubs.csv')
    total_df = pd.concat([
        transform_df(star_df, 'star'),
        transform_df(scrub_df, 'scrub')
    ])
    df_json = total_df.to_json(orient='records',lines=True)
    print(df_json)
    f = open('records.jsonl', 'w')
    f.write(df_json)
    
if __name__ == "__main__":
    main()
