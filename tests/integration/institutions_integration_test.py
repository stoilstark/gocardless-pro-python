# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import pytest
import requests
import responses

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_institutions_list():
    fixture = helpers.load_fixture('institutions')['list']
    helpers.stub_response(fixture)
    response = helpers.client.institutions.list(*fixture['url_params'])
    body = fixture['body']['institutions']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.Institution)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert [r.autocompletes_collect_bank_account for r in response.records] == [b.get('autocompletes_collect_bank_account') for b in body]
    assert [r.country_code for r in response.records] == [b.get('country_code') for b in body]
    assert [r.icon_url for r in response.records] == [b.get('icon_url') for b in body]
    assert [r.id for r in response.records] == [b.get('id') for b in body]
    assert [r.logo_url for r in response.records] == [b.get('logo_url') for b in body]
    assert [r.name for r in response.records] == [b.get('name') for b in body]

@responses.activate
def test_timeout_institutions_list_retries():
    fixture = helpers.load_fixture('institutions')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.institutions.list(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['institutions']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.Institution)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']

def test_502_institutions_list_retries():
    fixture = helpers.load_fixture('institutions')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.institutions.list(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['institutions']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.Institution)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']

@responses.activate
def test_institutions_all():
    fixture = helpers.load_fixture('institutions')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.institutions.all())
    assert len(all_records) == len(fixture['body']['institutions']) * 2
    for record in all_records:
      assert isinstance(record, resources.Institution)
    
  

@responses.activate
def test_institutions_list_for_billing_request():
    fixture = helpers.load_fixture('institutions')['list_for_billing_request']
    helpers.stub_response(fixture)
    response = helpers.client.institutions.list_for_billing_request(*fixture['url_params'])
    body = fixture['body']['institutions']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.Institution)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert [r.autocompletes_collect_bank_account for r in response.records] == [b.get('autocompletes_collect_bank_account') for b in body]
    assert [r.country_code for r in response.records] == [b.get('country_code') for b in body]
    assert [r.icon_url for r in response.records] == [b.get('icon_url') for b in body]
    assert [r.id for r in response.records] == [b.get('id') for b in body]
    assert [r.logo_url for r in response.records] == [b.get('logo_url') for b in body]
    assert [r.name for r in response.records] == [b.get('name') for b in body]

def test_timeout_institutions_list_for_billing_request_doesnt_retry():
    fixture = helpers.load_fixture('institutions')['list_for_billing_request']
    with helpers.stub_timeout(fixture) as rsps:
      with pytest.raises(requests.ConnectTimeout):
        response = helpers.client.institutions.list_for_billing_request(*fixture['url_params'])
      assert len(rsps.calls) == 1

def test_502_institutions_list_for_billing_request_doesnt_retry():
    fixture = helpers.load_fixture('institutions')['list_for_billing_request']
    with helpers.stub_502(fixture) as rsps:
      with pytest.raises(MalformedResponseError):
        response = helpers.client.institutions.list_for_billing_request(*fixture['url_params'])
      assert len(rsps.calls) == 1
  
