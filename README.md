# 🎯 **GrenadeHelperDataConverter** 

A tool for converting grenade data into YAML format, specifically designed for use with **Valthrun's Grenade Helper**. This script helps automate the configuration of grenade spots in your grenade helper by converting your raw input data into a structured format.

## 🚀 **Features**
- Convert grenade coordinate data into YAML format, ready for use with Valthrun's Grenade Helper.
- Automatically inserts the formatted data into `config.yaml` if present.
- Always generates a clean `output.txt` with grenade spot configurations, regardless of other config files.

## 📋 **Input Format**
The tool expects a `.txt` file where each line follows this format:

```
x1, y1, z1, type, x2, y2, z2, spot, map
```

### Example Input:
```txt
-1151.72,-1143.76,64.0312,Multiple,-1091.32,-670.314,1006.78,Right B (Jumpthrow),de_anubis
-1151.96,-1144,64.0312,Multiple,-1172.99,-629.352,985.175,Left B (Jumpthrow),de_anubis
-1169.68,-473.635,113.531,Temple B Smoke,-1055.76,327.347,758.437,throw,de_anubis
-1169.68,-473.635,113.531,Temple B,-1055.76,327.347,758.437,Throw,de_anubis
-1171.54,1159.4,52.7602,Donut Entrance,-1008.2,363.753,700.085,Throw,de_ancient
```

### Explanation:
- `x1, y1, z1`: Starting (eye) position coordinates.
- `type`: Type of grenade or action (e.g., Smoke, Flashbang, or "Multiple").
- `x2, y2, z2`: Target position coordinates.
- `spot`: The callout or spot name for the grenade throw.
- `map`: Map name (e.g., `de_anubis`, `de_ancient`).

## 💻 **Installation & Usage**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/valthrunner/GrenadeHelperDataConverter.git
   cd GrenadeHelperDataConverter
   ```

2. **Ensure Python 3.x is installed**.

3. **Run the script**:
   ```bash
   python converter.py
   ```

4. **Input file**: Ensure your input file follows the correct format and is placed in the current folder. The script will output the converted data in `output.txt`.

## ⚙️ **Config File Integration**

If a `config.yaml` file is present, the script will insert the generated data automatically.

### Example Output in `output.txt`:
```yaml
grenade_helpermap_spots:
  de_anubis:
  - grenade_types:
    - Multiple
    name: Right B (Jumpthrow)
    description: ''
    eye_position:
    - -1151.720
    - -1143.760
    - 126.031
    eye_direction:
    - -45.000
    - 160.000
  - grenade_types:
    - Multiple
    name: Left B (Jumpthrow)
    description: ''
    eye_position:
    - -1151.960
    - -1144.000
    - 126.031
    eye_direction:
    - -50.000
    - 165.000
```

## 🎥 Video Showcase

Check out how Valthrun's Grenade Helper works in action:

https://github.com/user-attachments/assets/6d458736-616e-4e3c-aa0f-fc4ced9756fb


