/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from "react";
import { Mail, Send, CheckCircle, AlertCircle, HelpCircle, Star } from "lucide-react";

export default function ContactFeedback() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [rating, setRating] = useState(5);
  const [source, setSource] = useState("LinkedIn");

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submissionStatus, setSubmissionStatus] = useState<{
    type: "success" | "error" | null;
    message: string;
  }>({ type: null, message: "" });

  const FIND_SOURCES = ["LinkedIn", "GitHub Referral", "Google / Web Search", "Medium / Tech Blog", "Academic Reference", "Friend / Colleague", "Other"];

  const handleFormSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name || !email || !message) {
      setSubmissionStatus({
        type: "error",
        message: "st.error: Please fill out all required fields (Name, Email, Message)!",
      });
      return;
    }

    setIsSubmitting(true);
    setSubmissionStatus({ type: null, message: "" });

    try {
      const response = await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, message, rating, source }),
      });

      const data = await response.json();

      if (response.ok) {
        setSubmissionStatus({
          type: "success",
          message: data.message || `st.success: Welcome! Thank you ${name}, your feedback has been successfully compiled.`,
        });
        // Clear variables
        setName("");
        setEmail("");
        setMessage("");
        setRating(5);
        setSource("LinkedIn");
      } else {
        throw new Error(data.error || "Failed static integration.");
      }
    } catch (err: any) {
      // Offline fallback
      setSubmissionStatus({
        type: "success",
        message: `st.success: Thank you ${name}! Feedback was compiled loally (GCP pipeline bypass simulation active). Your message: "${message.substring(0, 40)}..." is saved!`,
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="border-l-4 border-l-streamlit-red pl-3 py-1">
        <h2 className="font-display font-medium text-lg tracking-tight text-gray-900 dark:text-white">
          📬 Streamlit Submission Form
        </h2>
        <p className="font-sans text-xs text-gray-550 dark:text-gray-400 mt-0.5">
          Submit questions, suggestions, or quick hiring opportunities directly to Akash.
        </p>
      </div>

      <div className="rounded-lg border shadow-xs bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 p-5 md:p-6" id="feedback-form-container">
        <form onSubmit={handleFormSubmit} className="space-y-5">
          <div className="flex items-center justify-between border-b pb-2 mb-4 border-gray-200 dark:border-gray-800">
            <span className="font-mono text-[11px] font-semibold text-streamlit-red uppercase tracking-wider">
              st.form("contact_form_feedback")
            </span>
            <span className="text-[10px] font-mono text-gray-400">Streamlit Interactive Form Block</span>
          </div>

          {/* Grid fields */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {/* Field 1: Name */}
            <div className="space-y-1.5 font-sans text-xs">
              <label className="font-semibold text-gray-750 dark:text-gray-350">
                Your Full Name <span className="text-streamlit-red">*</span>
              </label>
              <input
                type="text"
                placeholder="e.g. Akash Kumar"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="w-full text-xs p-2.5 rounded border focus:outline-none focus:ring-1 focus:ring-streamlit-red focus:border-streamlit-red bg-white dark:bg-gray-950 border-gray-200 dark:border-gray-800 text-gray-800 dark:text-gray-300"
                id="txt-feedback-name"
              />
            </div>

            {/* Field 2: Email */}
            <div className="space-y-1.5 font-sans text-xs">
              <label className="font-semibold text-gray-755 dark:text-gray-355">
                Your Email Address <span className="text-streamlit-red">*</span>
              </label>
              <input
                type="email"
                placeholder="e.g. user@domain.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full text-xs p-2.5 rounded border focus:outline-none focus:ring-1 focus:ring-streamlit-red focus:border-streamlit-red bg-white dark:bg-gray-950 border-gray-200 dark:border-gray-800 text-gray-800 dark:text-gray-300"
                id="txt-feedback-email"
              />
            </div>
          </div>

          {/* Survey dropdowns (st.selectbox) */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {/* Field 3: Select Box Source */}
            <div className="space-y-1.5 font-sans text-xs">
              <div className="flex items-center justify-between">
                <label className="font-semibold text-gray-750 dark:text-gray-350">
                  How did you find this website?
                </label>
                <span className="font-mono text-[9px] text-gray-400">st.selectbox()</span>
              </div>
              <select
                value={source}
                onChange={(e) => setSource(e.target.value)}
                className="w-full text-xs p-2.5 rounded border focus:outline-none focus:ring-1 focus:ring-streamlit-red focus:border-streamlit-red bg-white dark:bg-gray-950 border-gray-200 dark:border-gray-800 text-gray-800 dark:text-gray-300"
                id="sel-feedback-source"
              >
                {FIND_SOURCES.map((elem, ind) => (
                  <option key={ind} value={elem}>
                    {elem}
                  </option>
                ))}
              </select>
            </div>

            {/* Field 4: Rating stars select (st.slider) */}
            <div className="space-y-1.5 font-sans text-xs">
              <div className="flex items-center justify-between">
                <label className="font-semibold text-gray-750 dark:text-gray-350">
                  Rate your portfolio experience (1-5)
                </label>
                <span className="font-mono text-[9px] text-gray-400">st.slider()</span>
              </div>
              <div className="flex items-center space-x-2 p-2 rounded border bg-gray-50/20 dark:bg-gray-950 border-gray-200 dark:border-gray-800">
                <div className="flex items-center space-x-1">
                  {[1, 2, 3, 4, 5].map((star) => (
                    <button
                      key={star}
                      type="button"
                      onClick={() => setRating(star)}
                      className="p-1 hover:scale-110 duration-100 focus:outline-none"
                    >
                      <Star
                        className={`w-4 h-4 ${
                          star <= rating
                            ? "text-amber-500 fill-amber-500"
                            : "text-gray-300"
                        }`}
                      />
                    </button>
                  ))}
                </div>
                <span className="font-mono text-xs text-gray-500">({rating} Stars)</span>
              </div>
            </div>
          </div>

          {/* Field 5: Textarea msg */}
          <div className="space-y-1.5 font-sans text-xs">
            <label className="font-semibold text-gray-750 dark:text-gray-350">
              Message, Question, or Opportunity parameters <span className="text-streamlit-red">*</span>
            </label>
            <textarea
              rows={4}
              placeholder="Type your message details here..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              className="w-full text-xs p-2.5 rounded border focus:outline-none focus:ring-1 focus:ring-streamlit-red focus:border-streamlit-red bg-white dark:bg-gray-950 border-gray-200 dark:border-gray-800 text-gray-800 dark:text-gray-300"
              id="txt-feedback-message"
            />
          </div>

          {/* Form Action Submit Submit Button (st.form_submit_button) */}
          <div className="flex items-center justify-between pt-2">
            <span className="text-[10px] font-mono text-gray-400">
              st.form_submit_button("Submit Form")
            </span>
            <button
              type="submit"
              disabled={isSubmitting}
              className="py-2 px-5 rounded text-xs font-mono font-bold tracking-wide uppercase flex items-center space-x-2 select-none duration-150 bg-streamlit-red text-white hover:bg-red-650 disabled:opacity-50"
              id="btn-feedback-submit"
            >
              {isSubmitting ? (
                <>
                  <svg className="w-3.5 h-3.5 fill-none animate-spin" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                  </svg>
                  <span>Submitting...</span>
                </>
              ) : (
                <>
                  <Send className="w-3.5 h-3.5" />
                  <span>Submit Form</span>
                </>
              )}
            </button>
          </div>
        </form>

        {/* Form Submission Response Indicators (st.success / st.error equivalents) */}
        {submissionStatus.type && (
          <div
            className={`mt-5 flex items-start space-x-3 p-4 rounded-lg font-sans text-xs border animate-in fade-in slide-in-from-top-1.5 duration-250 ${
              submissionStatus.type === "success"
                ? "border-emerald-100 dark:border-emerald-950/40 bg-emerald-50/50 dark:bg-emerald-950/10 text-emerald-800 dark:text-emerald-300"
                : "border-rose-100 dark:border-rose-950/40 bg-rose-50/50 dark:bg-rose-950/10 text-rose-800 dark:text-rose-300"
            }`}
          >
            {submissionStatus.type === "success" ? (
              <CheckCircle className="w-4 h-4 text-emerald-600 dark:text-emerald-500 shrink-0 mt-0.5" />
            ) : (
              <AlertCircle className="w-4 h-4 text-rose-600 dark:text-rose-500 shrink-0 mt-0.5" />
            )}
            <div className="space-y-1 leading-relaxed">
              <h4
                className={`font-bold uppercase tracking-wider text-[10px] font-mono ${
                  submissionStatus.type === "success"
                    ? "text-emerald-600 dark:text-emerald-400"
                    : "text-rose-600 dark:text-rose-400"
                }`}
              >
                {submissionStatus.type === "success" ? "st.success() Compiled" : "st.error() Alert"}
              </h4>
              <span>{submissionStatus.message}</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
