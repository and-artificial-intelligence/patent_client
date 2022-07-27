import pytest
from pathlib import Path
import json
from .api import PublishedDataApi, PublishedSearchApi, PublishedFulltextApi
from patent_client.util.test import compare_dicts

expected_dir = Path(__file__).parent / "test" / "expected"

def test_doc_example_biblio():
    result = PublishedDataApi.get_biblio("EP1000000.A1", format="epodoc")
    expected = json.loads((expected_dir / "ep1000000_biblio_result.json").read_text())
    compare_dicts(json.loads(result.to_json()), expected)

def test_doc_example_full_cycle():
    result = PublishedDataApi.get_full_cycle("EP1000000.A1", format="epodoc")
    expected = json.loads((expected_dir / "ep1000000_full_cycle_result.json").read_text())
    compare_dicts(json.loads(result.to_json()), expected)

def test_doc_example_abstract():
    result = PublishedDataApi.get_abstract("EP1000000.A1", format="epodoc")
    expected = json.loads((expected_dir / "ep1000000_abstract_result.json").read_text())
    compare_dicts(json.loads(result.to_json()), expected)

def test_doc_example_abstract():
    result = PublishedDataApi.get_abstract("EP1000000.A1", format="epodoc")
    expected = json.loads((expected_dir / "ep1000000_abstract_result.json").read_text())
    compare_dicts(json.loads(result.to_json()), expected)

def test_search():
    result = PublishedSearchApi.search("ti=plastic")
    with pytest.warns(None, match=r"OPS stops counting"):
        assert len(result) == 10000

    sample = result[5:10]
    assert len(sample) == 5

def test_search():
    result = PublishedSearchApi.search("ti=plastic")
    with pytest.warns(None, match=r"OPS stops counting"):
        assert len(result) == 10000

    sample = result[5:10]
    assert len(sample) == 5

def test_description():
    result = PublishedFulltextApi.get_description("EP1000000.A1", format="epodoc")
    expected = json.loads((expected_dir / "ep1000000_description_result.json").read_text())
    compare_dicts(json.loads(result.to_json()), expected)

def test_claims():
    result = PublishedFulltextApi.get_claims("EP1000000.A1", format="epodoc") 
    expected = json.loads((expected_dir / "ep1000000_claims_result.json").read_text())
    compare_dicts(json.loads(result.to_json()), expected)