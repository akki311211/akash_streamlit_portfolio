/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from "react";
import { TrendingUp, Award, Briefcase, Database } from "lucide-react";
import { Metric } from "../types";

interface MetricsBoardProps {
  metrics: Metric[];
  aiConfidenceValue: number;
}

export default function MetricsBoard({ metrics, aiConfidenceValue }: MetricsBoardProps) {
  // We can calculate dynamic subelements to adapt to user sidebar sliders!
  const getDynamicMetricValue = (label: string, fallbackVal: string) => {
    if (label.includes("SQL")) {
      const scaledRows = (2.5 * (aiConfidenceValue / 80)).toFixed(2);
      return `~${scaledRows}M Recs/day`;
    }
    if (label.includes("Vite")) {
      const activeApps = Math.floor(20 + (aiConfidenceValue - 80) / 3);
      return `${activeApps}+ Live`;
    }
    return fallbackVal;
  };

  return (
    <div className="space-y-4">
      <div className="border-l-4 border-l-streamlit-red pl-3 py-1">
        <h2 className="font-display font-medium text-lg tracking-tight text-gray-900 dark:text-white">
          📈 Live Analytical Metrics
        </h2>
        <p className="font-sans text-xs text-gray-500 dark:text-gray-400 mt-0.5">
          Dynamic KPIs updated automatically based on core parameters.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4" id="metrics-grid">
        {metrics.map((metric, idx) => {
          const isPositive = metric.deltaType !== "negative";
          const subLabel = getDynamicMetricValue(metric.label, metric.delta || "");

          return (
            <div
              key={idx}
              className="p-5 rounded-lg border shadow-xs transition-transform hover:scale-[1.01] hover:shadow-sm duration-200 bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800"
            >
              {/* Metric Card Header */}
              <div className="flex items-center justify-between text-gray-400 dark:text-gray-500 mb-2">
                <span className="font-sans font-semibold text-xs py-0.5 uppercase tracking-wide">
                  {metric.label}
                </span>
                <span className="text-sm" role="img" aria-label={metric.label}>
                  {metric.emoji || "📊"}
                </span>
              </div>

              {/* Metric Big Value Segment */}
              <div className="font-display font-bold text-2xl md:text-3xl text-gray-900 dark:text-white mb-2 font-semibold">
                {metric.value}
              </div>

              {/* Delta Value Element resembling st.metric trajectory highlights */}
              <div className="flex items-center space-x-1.5 font-mono text-xs">
                {isPositive ? (
                  <TrendingUp className="w-3.5 h-3.5 text-emerald-500 stroke-[2.5]" />
                ) : (
                  <TrendingUp className="w-3.5 h-3.5 text-rose-500 rotate-180 stroke-[2.5]" />
                )}
                <span
                  className={
                    isPositive
                      ? "text-emerald-600 dark:text-emerald-400 font-medium"
                      : "text-rose-600 dark:text-rose-400 font-medium"
                  }
                >
                  {subLabel}
                </span>
              </div>
            </div>
          );
        })}
      </div>

      {/* Embedded Streamlit Alert-box (st.info) */}
      <div className="flex items-start space-x-3 p-4 rounded-lg font-sans text-xs border border-sky-100 dark:border-sky-950/40 bg-sky-50/50 dark:bg-sky-955/20 text-sky-800 dark:text-sky-300">
        <span className="text-base select-none mt-0.5">💡</span>
        <div className="space-y-1 leading-relaxed">
          <p className="font-bold uppercase tracking-wider text-[10px] font-mono text-sky-600 dark:text-sky-400 mb-0.5">
            st.info() - Parameter Calibration
          </p>
          <span>
            Adjusting the <strong>"Target AI Precision Match"</strong> slider in the left sidebar will recalibrate Akash's computational metrics, showcasing standard Streamlit state management synchronization.
          </span>
        </div>
      </div>
    </div>
  );
}
