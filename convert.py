import re
import math
import os

VALID_GRENADE_TYPES = ['Flashbang', 'Smoke', 'Molotov', 'Explosive']
PLAYER_HEIGHT_OFFSET = 62

def convert_to_pitch_yaw(x1, y1, z1, x2, y2, z2):
    dz = z2 - (z1 + PLAYER_HEIGHT_OFFSET)
    yaw = (math.degrees(math.atan2(y2 - y1, x2 - x1)) + 360) % 360
    pitch = math.degrees(math.atan2(-dz, math.hypot(x2 - x1, y2 - y1)))
    return round(pitch, 3), round(yaw, 3)

def parse_float_coordinates(*coords):
    return [f"{float(c):.3f}" for c in coords]

def process_grenade_data(input_file, output_file):
    pattern = re.compile(r'([-.\d]+),([-.\d]+),([-.\d]+),([\w\s()]+),([-.\d]+),([-.\d]+),([-.\d]+),([a-zA-Z ()0-9+&]+),de_([a-zA-Z0-9_]+)')
    data = {}

    try:
        with open(input_file, 'r') as file:
            for line in file:
                match = pattern.match(line)
                if match:
                    x1, y1, z1, name, x2, y2, z2, details, map_name = match.groups()
                    g_type = next((gt for gt in VALID_GRENADE_TYPES if f"({gt})" in details), None)
                    if g_type:
                        pitch, yaw = convert_to_pitch_yaw(float(x1), float(y1), float(z1), float(x2), float(y2), float(z2))
                        spot = {
                            'name': f"{name.strip()} {details.replace(f'({g_type})', '').strip()}".strip(),
                            'grenade_types': [g_type],
                            'eye_position': parse_float_coordinates(x1, y1, float(z1) + PLAYER_HEIGHT_OFFSET),
                            'eye_direction': [f"{pitch:.3f}", f"{yaw:.3f}"],
                            'description': ''
                        }
                        data.setdefault(map_name, []).append(spot)

        output = ['grenade_helpermap_spots:\n']
        for map_name, spots in data.items():
            output.append(f'  de_{map_name}:\n')
            for spot in spots:
                output.append(f'  - grenade_types:\n    - {spot["grenade_types"][0]}\n')
                output.append(f'    name: {spot["name"]}\n    description: \'{spot["description"]}\'\n')
                output.append(f'    eye_position:\n')
                output.extend(f'    - {pos}\n' for pos in spot["eye_position"])
                output.append(f'    eye_direction:\n')
                output.extend(f'    - {dir}\n' for dir in spot["eye_direction"])

        with open(output_file, 'w') as file:
            file.write(''.join(output))

        return ''.join(output)

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

def insert_into_config(output_text):
    config_file = 'config.yaml'
    if not os.path.exists(config_file):
        print("No config.yaml found, skipping insertion.")
        return

    try:
        with open(config_file, 'r') as file:
            config_lines = file.readlines()

        start_index = next((i for i, line in enumerate(config_lines) if 'grenade_helpercolor_angle_active' in line), None)
        end_index = next((i for i, line in enumerate(config_lines) if 'imgui:' in line), None)

        if start_index is not None and end_index is not None:
            config_lines = config_lines[:start_index + 1] + [output_text] + config_lines[end_index:]

            with open(config_file, 'w') as file:
                file.write(''.join(config_lines))
            print("Output inserted into config.yaml successfully.")
        else:
            print("Could not find proper insertion points in config.yaml.")

    except Exception as e:
        print(f"An error occurred while updating config.yaml: {e}")

def main():
    input_file = 'GrenadeHelper.txt'
    
    if not os.path.exists(input_file):
        input_file = input(f"{input_file} not found. Please provide the path to another text file: ").strip()
        if not os.path.exists(input_file):
            print("File not found. Exiting.")
            return

    output_file = 'output.txt'
    output_text = process_grenade_data(input_file, output_file)

    if output_text:
        insert_into_config(output_text)
        print(f"Output generated in {output_file}")

if __name__ == "__main__":
    main()
