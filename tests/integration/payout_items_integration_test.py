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
def test_payout_items_list():
    fixture = helpers.load_fixture('payout_items')['list']
    helpers.stub_response(fixture)
    response = helpers.client.payout_items.list(*fixture['url_params'])
    body = fixture['body']['payout_items']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.PayoutItem)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']
    assert responses.calls[-1].request.headers.get('Idempotency-Key') is None
    assert [r.amount for r in response.records] == [b.get('amount') for b in body]
    assert [r.taxes for r in response.records] == [b.get('taxes') for b in body]
    assert [r.type for r in response.records] == [b.get('type') for b in body]

@responses.activate
def test_timeout_payout_items_list_retries():
    fixture = helpers.load_fixture('payout_items')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.payout_items.list(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['payout_items']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.PayoutItem)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']

def test_502_payout_items_list_retries():
    fixture = helpers.load_fixture('payout_items')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.payout_items.list(*fixture['url_params'])
      assert len(rsps.calls) == 2
      assert rsps.calls[0].request.headers.get('Idempotency-Key') == rsps.calls[1].request.headers.get('Idempotency-Key')
    body = fixture['body']['payout_items']

    assert isinstance(response, list_response.ListResponse)
    assert isinstance(response.records[0], resources.PayoutItem)

    assert response.before == fixture['body']['meta']['cursors']['before']
    assert response.after == fixture['body']['meta']['cursors']['after']

@responses.activate
def test_payout_items_all():
    fixture = helpers.load_fixture('payout_items')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.payout_items.all())
    assert len(all_records) == len(fixture['body']['payout_items']) * 2
    for record in all_records:
      assert isinstance(record, resources.PayoutItem)
    
  
