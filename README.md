# Database Schema Documentation Generator

This Python tool connects to a PostgreSQL database using a connection string provided via an environment variable and generates a Markdown (.md) file documenting the database schema. The generated documentation includes a list of tables and their columns, along with placeholders for descriptions that can be filled in later.

## Features

- Connects to a PostgreSQL database using a connection string from an environment variable.
- Retrieves all tables and their columns from the database.
- Generates a `.md` file documenting the database schema.
- Provides a structured format for easy documentation of database schemas.

## Prerequisites

- Python 3.x
- PostgreSQL database
- The following Python packages:
  - `psycopg2`
  - `pandas`

You can install the required Python packages using pip:

```bash
pip install psycopg2 pandas
```

## Getting Started

### 1. Set Up the Environment

Ensure that the `DB_CONNECTION_STRING` environment variable is set in your environment. This variable should contain the connection string for your PostgreSQL database.

#### Linux/MacOS:

```bash
export DB_CONNECTION_STRING="dbname='yourdbname' user='yourusername' password='yourpassword' host='yourhost' port='yourport'"
```

#### Windows:

```cmd
set DB_CONNECTION_STRING="dbname='yourdbname' user='yourusername' password='yourpassword' host='yourhost' port='yourport'"
```

### 2. Run the Script

Once the environment variable is set, you can run the script to generate the database schema documentation:

```bash
python generate_schema.py
```

The script will generate a Markdown file named `database_schema.md` in the current directory.

### 3. Customize the Documentation

After generating the `database_schema.md` file, open it in your preferred text editor and fill in the descriptions for each table and column as needed.

## Example Output

Below is an example of the generated documentation format:

```markdown
# **Database Schema Documentation**

## **Overview**

This document outlines the structure and purpose of each table in the database.

## **Tables Overview**

1. **MyTable1**
2. **MyTable2**
3. **MyTable3**
   ...

---

### **1. MyTable1**

**Description:**

| Column Name | Data Type    | Description |
| ----------- | ------------ | ----------- |
| Col1        | INT          |             |
| Col2        | VARCHAR(255) |             |
| Col3        | INT          |             |
| Col4        | TIMESTAMP    |             |
| Col5        | TIMESTAMP    |             |

...
```

## Customization

- **Database Engine**: The current script is configured for PostgreSQL. If you're using a different database engine, you'll need to modify the connection method accordingly.
- **Output File**: You can change the output file name and path by modifying the `output_file` variable in the script.
- **Environment Variable Name**: If you prefer a different name for the environment variable, you can change `DB_CONNECTION_STRING` to your preferred name in the script.

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request. Bug reports and feature requests are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for clear and structured database documentation.
