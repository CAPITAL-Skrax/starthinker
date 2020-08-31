###########################################################################
# 
#  Copyright 2019 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

'''
--------------------------------------------------------------

Before running this Airflow module...

  Install StarThinker in cloud composer from open source: 

    pip install git+https://github.com/google/starthinker

  Or push local code to the cloud composer plugins directory:

    source install/deploy.sh
    4) Composer Menu	   
    l) Install All

--------------------------------------------------------------

Email Fetch

Import emailed CM report, Dv360 report, csv, or excel into a BigQuery table.

The person executing this recipe must be the recipient of the email.
Give a regular expression to match the email subject, link or attachment.
The data downloaded will overwrite the table specified.

'''

from starthinker_airflow.factory import DAG_Factory
 
# Add the following credentials to your Airflow configuration.
USER_CONN_ID = "starthinker_user" # The connection to use for user authentication.
GCP_CONN_ID = "starthinker_service" # The connection to use for service authentication.

INPUTS = {
  'auth_read': 'user',  # Credentials used for reading data.
  'email_from': '',  # Must match from field.
  'email_to': '',  # Must match to field.
  'subject': '',  # Regular expression to match subject.
  'link': '',  # Regular expression to match email.
  'attachment': '',  # Regular expression to match atttachment.
  'dataset': '',  # Existing dataset in BigQuery.
  'table': '',  # Name of table to be written to.
  'dbm_schema': '[]',  # Schema provided in JSON list format or empty list.
  'is_incremental_load': False,  # Append report data to table based on date column, de-duplicates.
}

TASKS = [
  {
    'email': {
      'auth': {
        'field': {
          'name': 'auth_read',
          'kind': 'authentication',
          'order': 1,
          'default': 'user',
          'description': 'Credentials used for reading data.'
        }
      },
      'read': {
        'from': {
          'field': {
            'name': 'email_from',
            'kind': 'string',
            'order': 1,
            'default': '',
            'description': 'Must match from field.'
          }
        },
        'to': {
          'field': {
            'name': 'email_to',
            'kind': 'string',
            'order': 2,
            'default': '',
            'description': 'Must match to field.'
          }
        },
        'subject': {
          'field': {
            'name': 'subject',
            'kind': 'string',
            'order': 3,
            'default': '',
            'description': 'Regular expression to match subject.'
          }
        },
        'link': {
          'field': {
            'name': 'link',
            'kind': 'string',
            'order': 4,
            'default': '',
            'description': 'Regular expression to match email.'
          }
        },
        'attachment': {
          'field': {
            'name': 'attachment',
            'kind': 'string',
            'order': 5,
            'default': '',
            'description': 'Regular expression to match atttachment.'
          }
        }
      },
      'out': {
        'bigquery': {
          'dataset': {
            'field': {
              'name': 'dataset',
              'kind': 'string',
              'order': 6,
              'default': '',
              'description': 'Existing dataset in BigQuery.'
            }
          },
          'table': {
            'field': {
              'name': 'table',
              'kind': 'string',
              'order': 7,
              'default': '',
              'description': 'Name of table to be written to.'
            }
          },
          'schema': {
            'field': {
              'name': 'dbm_schema',
              'kind': 'json',
              'order': 8,
              'default': '[]',
              'description': 'Schema provided in JSON list format or empty list.'
            }
          },
          'is_incremental_load': {
            'field': {
              'name': 'is_incremental_load',
              'kind': 'boolean',
              'order': 9,
              'default': False,
              'description': 'Append report data to table based on date column, de-duplicates.'
            }
          }
        }
      }
    }
  }
]

DAG_FACTORY = DAG_Factory('email_to_bigquery', { 'tasks':TASKS }, INPUTS)
DAG_FACTORY.apply_credentails(USER_CONN_ID, GCP_CONN_ID)
DAG = DAG_FACTORY.execute()

if __name__ == "__main__":
  DAG_FACTORY.print_commandline()
