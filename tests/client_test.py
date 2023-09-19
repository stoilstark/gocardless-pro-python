# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import pytest
import requests
import responses

from gocardless_pro import Client
from gocardless_pro import services

access_token = 'access-token-xyz'
client = Client(access_token=access_token, base_url='http://example.com')

def test_requires_valid_environment():
    with pytest.raises(ValueError):
        Client(access_token=access_token, environment='invalid')


def test_bank_authorisations_returns_service():
    assert isinstance(client.bank_authorisations, services.BankAuthorisationsService)

def test_bank_details_lookups_returns_service():
    assert isinstance(client.bank_details_lookups, services.BankDetailsLookupsService)

def test_billing_requests_returns_service():
    assert isinstance(client.billing_requests, services.BillingRequestsService)

def test_billing_request_flows_returns_service():
    assert isinstance(client.billing_request_flows, services.BillingRequestFlowsService)

def test_billing_request_templates_returns_service():
    assert isinstance(client.billing_request_templates, services.BillingRequestTemplatesService)

def test_blocks_returns_service():
    assert isinstance(client.blocks, services.BlocksService)

def test_creditors_returns_service():
    assert isinstance(client.creditors, services.CreditorsService)

def test_creditor_bank_accounts_returns_service():
    assert isinstance(client.creditor_bank_accounts, services.CreditorBankAccountsService)

def test_currency_exchange_rates_returns_service():
    assert isinstance(client.currency_exchange_rates, services.CurrencyExchangeRatesService)

def test_customers_returns_service():
    assert isinstance(client.customers, services.CustomersService)

def test_customer_bank_accounts_returns_service():
    assert isinstance(client.customer_bank_accounts, services.CustomerBankAccountsService)

def test_customer_notifications_returns_service():
    assert isinstance(client.customer_notifications, services.CustomerNotificationsService)

def test_events_returns_service():
    assert isinstance(client.events, services.EventsService)

def test_instalment_schedules_returns_service():
    assert isinstance(client.instalment_schedules, services.InstalmentSchedulesService)

def test_institutions_returns_service():
    assert isinstance(client.institutions, services.InstitutionsService)

def test_mandates_returns_service():
    assert isinstance(client.mandates, services.MandatesService)

def test_mandate_imports_returns_service():
    assert isinstance(client.mandate_imports, services.MandateImportsService)

def test_mandate_import_entries_returns_service():
    assert isinstance(client.mandate_import_entries, services.MandateImportEntriesService)

def test_mandate_pdfs_returns_service():
    assert isinstance(client.mandate_pdfs, services.MandatePdfsService)

def test_negative_balance_limits_returns_service():
    assert isinstance(client.negative_balance_limits, services.NegativeBalanceLimitsService)

def test_payer_authorisations_returns_service():
    assert isinstance(client.payer_authorisations, services.PayerAuthorisationsService)

def test_payments_returns_service():
    assert isinstance(client.payments, services.PaymentsService)

def test_payouts_returns_service():
    assert isinstance(client.payouts, services.PayoutsService)

def test_payout_items_returns_service():
    assert isinstance(client.payout_items, services.PayoutItemsService)

def test_redirect_flows_returns_service():
    assert isinstance(client.redirect_flows, services.RedirectFlowsService)

def test_refunds_returns_service():
    assert isinstance(client.refunds, services.RefundsService)

def test_scenario_simulators_returns_service():
    assert isinstance(client.scenario_simulators, services.ScenarioSimulatorsService)

def test_scheme_identifiers_returns_service():
    assert isinstance(client.scheme_identifiers, services.SchemeIdentifiersService)

def test_subscriptions_returns_service():
    assert isinstance(client.subscriptions, services.SubscriptionsService)

def test_tax_rates_returns_service():
    assert isinstance(client.tax_rates, services.TaxRatesService)

def test_verification_details_returns_service():
    assert isinstance(client.verification_details, services.VerificationDetailsService)

def test_webhooks_returns_service():
    assert isinstance(client.webhooks, services.WebhooksService)

