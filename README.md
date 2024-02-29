# Radio.garden -> m3u
A software that creates a m3u playlist from radio.garden public API data.

## Pre-requisites

- Python

## How to use

1. Clone the repository

```bash
git clone https://github.com/ovosimpatico/radio.garden-to-m3u.git
```

2. Run the script

```bash
python main.py --country COUNTRY --state STATE
```

The m3u file will be created in the same directory as the script, as radio.m3u. It can be used on any player that supports m3u playlists, such as VLC or MPV.

Examples:

```bash
python main.py --country "Brazil" --state "SP"
```

```bash
python main.py --country "United States" --state "LA"
```

```bash
python main.py --country "Bulgaria"
```

## License

This project is licensed under the Affero General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is not affiliated with radio.garden in any way. It uses the public API provided by the website to create a m3u playlist.

## Acknowledgements

- [radio-garden-openapi](https://github.com/jonasrmichel/radio-garden-openapi)