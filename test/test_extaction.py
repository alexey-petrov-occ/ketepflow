import pytest
import jsonschema as js
from metafoam import json_format

models_schema = \
 {
  "definitions": {
    'attr': {
      "type": "string",
    },
    "attrs": {
      "type": "array",
      "items": [
        {
          "$ref": "#/definitions/attr"
        }
      ]
    },
    'model': {
      'type': 'object', 'properties': {
        'name': {'type': 'string'},
        'attrs': {'$ref': '#/definitions/attrs'},
      }
    },
    "name": {
      "type": "string",
    },
    "names": {
      "type": "array",
      "items": [
        {
          "$ref": "#/definitions/name"
        }
      ]
    },
    'category': {
      'type': 'object', 'properties': {
        'name': {'type': 'string'},
        'models': {"$ref": "#/definitions/names"}
      }
    }
  },
  'title': 'core',
  'type': 'object', 'properties': {
    'transport': {'type': 'object', 'properties': {
      'models': {"type": "array", "items": [{"$ref": "#/definitions/model"}]},
      'categories':
          {"type": "array", "items": [{"$ref": "#/definitions/category"}]}

    }}
  },
  "required": ["transport"],
  "minProperties": 1, "maxProperties": 1,
 }


def test_translation():
    with pytest.raises(js.exceptions.ValidationError):
        source = {'a': ['x', 'y'], 'b': ['z'], 'c': []}
        js.validate(source, models_schema)

    with pytest.raises(js.exceptions.ValidationError):
        source = {'transport': {}, 'x': {}}
        js.validate(source, models_schema)

    Source = {'a': ['x', 'y'], 'b': ['z'], 'c': []}
    js.validate(json_format.handler_json(Source), models_schema)

    # target = {'transport': {
    #   'models': [{'name': 'a', 'attrs': ['x', 'y']},
    #              {'name': 'b', 'attrs': ['z']},
    #              {'name': 'c', 'attrs': []}],
    #   'categories': [{'name': 'K', 'models': ['b']},
    #                  {'name': 'L', 'models': ['a', 'c']}]
    # }}
