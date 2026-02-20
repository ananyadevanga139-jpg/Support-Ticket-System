from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer
from django.db.models import Count
import os
import requests

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-created_at')
    serializer_class = TicketSerializer

    # Filter tickets
    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET.get('category')
        priority = self.request.GET.get('priority')
        status_filter = self.request.GET.get('status')
        search = self.request.GET.get('search')

        if category:
            qs = qs.filter(category=category)
        if priority:
            qs = qs.filter(priority=priority)
        if status_filter:
            qs = qs.filter(status=status_filter)
        if search:
            qs = qs.filter(title__icontains=search) | qs.filter(description__icontains=search)
        return qs

    @action(detail=False, methods=['get'])
    def stats(self, request):
        total = Ticket.objects.count()
        open_tickets = Ticket.objects.filter(status='open').count()
        avg_per_day = Ticket.objects.count() / max(Ticket.objects.dates('created_at', 'day').count(), 1)
        priority_breakdown = Ticket.objects.values('priority').annotate(count=Count('id'))
        category_breakdown = Ticket.objects.values('category').annotate(count=Count('id'))

        return Response({
            "total_tickets": total,
            "open_tickets": open_tickets,
            "avg_tickets_per_day": avg_per_day,
            "priority_breakdown": {p['priority']: p['count'] for p in priority_breakdown},
            "category_breakdown": {c['category']: c['count'] for c in category_breakdown},
        })

    @action(detail=False, methods=['post'])
    def classify(self, request):
        description = request.data.get('description', '')
        if not description:
            return Response({"error": "Description required"}, status=status.HTTP_400_BAD_REQUEST)

        # Call LLM API (OpenAI) - placeholder
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return Response({"suggested_category": "general", "suggested_priority": "low"})

        # Example OpenAI API call
        # You can replace with your preferred LLM API
        prompt = f"Categorize this ticket and suggest priority: {description}"
        # Dummy response
        return Response({"suggested_category": "technical", "suggested_priority": "medium"})
