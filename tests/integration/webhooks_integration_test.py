# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_not_equal,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_webhooks_list():
    fixture = helpers.load_fixture('webhooks')['list']
    helpers.stub_response(fixture)
    response = helpers.client.webhooks.list(*fixture['url_params'])
    body = fixture['body']['webhooks']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Webhook)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.is_test for r in response.records],
                 [b.get('is_test') for b in body])
    assert_equal([r.request_body for r in response.records],
                 [b.get('request_body') for b in body])
    assert_equal([r.request_headers for r in response.records],
                 [b.get('request_headers') for b in body])
    assert_equal([r.response_body for r in response.records],
                 [b.get('response_body') for b in body])
    assert_equal([r.response_body_truncated for r in response.records],
                 [b.get('response_body_truncated') for b in body])
    assert_equal([r.response_code for r in response.records],
                 [b.get('response_code') for b in body])
    assert_equal([r.response_headers for r in response.records],
                 [b.get('response_headers') for b in body])
    assert_equal([r.response_headers_content_truncated for r in response.records],
                 [b.get('response_headers_content_truncated') for b in body])
    assert_equal([r.response_headers_count_truncated for r in response.records],
                 [b.get('response_headers_count_truncated') for b in body])
    assert_equal([r.successful for r in response.records],
                 [b.get('successful') for b in body])
    assert_equal([r.url for r in response.records],
                 [b.get('url') for b in body])

@responses.activate
def test_timeout_webhooks_list_retries():
    fixture = helpers.load_fixture('webhooks')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.webhooks.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['webhooks']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Webhook)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_webhooks_list_retries():
    fixture = helpers.load_fixture('webhooks')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.webhooks.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['webhooks']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Webhook)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_webhooks_all():
    fixture = helpers.load_fixture('webhooks')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.webhooks.all())
    assert_equal(len(all_records), len(fixture['body']['webhooks']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.Webhook)
    
  

@responses.activate
def test_webhooks_get():
    fixture = helpers.load_fixture('webhooks')['get']
    helpers.stub_response(fixture)
    response = helpers.client.webhooks.get(*fixture['url_params'])
    body = fixture['body']['webhooks']

    assert_is_instance(response, resources.Webhook)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.is_test, body.get('is_test'))
    assert_equal(response.request_body, body.get('request_body'))
    assert_equal(response.request_headers, body.get('request_headers'))
    assert_equal(response.response_body, body.get('response_body'))
    assert_equal(response.response_body_truncated, body.get('response_body_truncated'))
    assert_equal(response.response_code, body.get('response_code'))
    assert_equal(response.response_headers, body.get('response_headers'))
    assert_equal(response.response_headers_content_truncated, body.get('response_headers_content_truncated'))
    assert_equal(response.response_headers_count_truncated, body.get('response_headers_count_truncated'))
    assert_equal(response.successful, body.get('successful'))
    assert_equal(response.url, body.get('url'))

@responses.activate
def test_timeout_webhooks_get_retries():
    fixture = helpers.load_fixture('webhooks')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.webhooks.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['webhooks']

    assert_is_instance(response, resources.Webhook)

def test_502_webhooks_get_retries():
    fixture = helpers.load_fixture('webhooks')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.webhooks.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['webhooks']

    assert_is_instance(response, resources.Webhook)
  

@responses.activate
def test_webhooks_retry():
    fixture = helpers.load_fixture('webhooks')['retry']
    helpers.stub_response(fixture)
    response = helpers.client.webhooks.retry(*fixture['url_params'])
    body = fixture['body']['webhooks']

    assert_is_instance(response, resources.Webhook)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.is_test, body.get('is_test'))
    assert_equal(response.request_body, body.get('request_body'))
    assert_equal(response.request_headers, body.get('request_headers'))
    assert_equal(response.response_body, body.get('response_body'))
    assert_equal(response.response_body_truncated, body.get('response_body_truncated'))
    assert_equal(response.response_code, body.get('response_code'))
    assert_equal(response.response_headers, body.get('response_headers'))
    assert_equal(response.response_headers_content_truncated, body.get('response_headers_content_truncated'))
    assert_equal(response.response_headers_count_truncated, body.get('response_headers_count_truncated'))
    assert_equal(response.successful, body.get('successful'))
    assert_equal(response.url, body.get('url'))

def test_timeout_webhooks_retry_doesnt_retry():
    fixture = helpers.load_fixture('webhooks')['retry']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.webhooks.retry(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_webhooks_retry_doesnt_retry():
    fixture = helpers.load_fixture('webhooks')['retry']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.webhooks.retry(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  
